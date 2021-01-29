from django.db.models import fields
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .forms import RegistrationForm
from .models import Feedback, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View


from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .serializers import CommentSerializer, UserSerializer, FeedbackSerializer
from django.contrib.auth.models import User

from main import serializers
from django.contrib.auth import authenticate

class MainView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='main/index.html'
        )


class AboutView(View):
   def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='main/about.html'
        )


def registration(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            form = registration_form.save(commit=False)
            form.first_name = registration_form.cleaned_data["first_name"]
            form.last_name = registration_form.cleaned_data["last_name"]
            form.email = registration_form.cleaned_data["email"]
            form.save()
            return redirect('main:main')

    else:
        registration_form = RegistrationForm()

    return render(
        request=request,
        template_name='main/registration.html',
        context={"sign_in_form": registration_form}
    )


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'main/feedback_list.html'

    def get_queryset(self, *args, **kwargs):
        overried_queryset = super(FeedbackListView, self).get_queryset(*args, **kwargs)
        result = overried_queryset.order_by('-date_created')
        return result


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name='main/feedback_details.html'

    def get_context_data(self, **kwargs):
        feedback = self.get_object()
        kwargs['comment_list'] = Comment.objects.filter(assigned_to_feedback=feedback.pk)
        return super().get_context_data(**kwargs)


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['feedback_text',]
    template_name = 'main/feedback_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class FeedbackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Feedback
    fields = ['feedback_text',]
    template_name = 'main/feedback_update.html'

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False


class FeedbackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Feedback
    success_url = "/feedbacks/"
    template_name = 'main/feedback_delete.html'

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False





####################################################################################################
####################################### Django REST API ############################################
####################################################################################################

class UserListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    queryset = User.objects.all()


class UserDetailsAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.filter(username=request.user).first()
        if user:
            return Response(
                data={
                    "success": True,
                    "result": user
                },
                status=status.HTTP_200_OK
            )
        return Response(
                data={
                    "success": False,
                    "result": "Ты кто такой?"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )



class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def put(self, request):
        user = User.objects.get(id=request.data.get('id'))
        serializer = self.serializer_class(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "success": True,
                "result": "User has been UPDATED successfully!"
            }
        )


class UserDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def delete(self, request):
        user = User.objects.get(id=request.data.get('id'))
        user.delete()
        return Response(
            data={
                "success": True,
                "result": "User has been DELETED successfully!"
            }
        )


class FeedbackListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()



class FeedbackCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = FeedbackSerializer

    def post(self, request):
        try:
            if request.data.get('author_id'):
                user = User.objects.get(pk=request.data.get('author_id'))
                author_id = user.pk
            else:
                author_id = None

        except User.DoesNotExist:
            return Response(
            data={
                "success":False,
                "result":"Такого пользователя нет в Базе Данных или Вы не указали author_id."
            },
            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
        )


        serializer = FeedbackSerializer(
            data=request.data, 
            context={
                "author_id": author_id,
                "request": request
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                "success":True,
                "result":"Отзыв был оставлен успешно"
            },
            status=status.HTTP_201_CREATED
        )



class FeedbackUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer

    def put(self, request):
        try:
            feedback_id = Feedback.objects.get(pk=request.data.get('feedback_id'))

            serializer = FeedbackSerializer(
                instance=feedback_id,
                data=request.data,
                partial=True
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                data={
                    "success":True,
                    "result":"Отзыв был ОБНОВЛЁН успешно"
                },
                status=status.HTTP_200_OK
            )
        except Feedback.DoesNotExist:
            return Response(
            data={
                "success":False,
                "result":"Отзыв не найден!"
            },
            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
        )


class FeedbackDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer

    def delete(self, request):
        try:
            feedback_id = Feedback.objects.get(pk=request.data.get('feedback_id'))
            feedback_id.delete()
            return Response(
                data={
                    "success":True,
                    "result":"Отзыв был УДАЛЁН успешно"
                },
                status=status.HTTP_202_ACCEPTED
            )
        except Feedback.DoesNotExist:
            return Response(
            data={
                "success":False,
                "result":"Отзыв не найден!"
            },
            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
        )



class CommentListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get(self, request):
        serializer = self.serializer_class(Comment.objects.all(), many=True)
        return Response(
            data={
                "success": True,
                "result": serializer.data
            }
        )

class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get(self, request):
        serializer = self.serializer_class(Comment.objects.all(), many=True)
        return Response(
            data={
                "success": True,
                "result": serializer.data
            }
        )

class CommentListAPIView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get(self, request):
        serializer = self.serializer_class(Comment.objects.all(), many=True)
        return Response(
            data={
                "success": True,
                "result": serializer.data
            }
        )

class CommentListAPIView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def delete(self, request):
    
        return Response(
            data={
                "success": True,
                "result": serializer.data
            } 
        )