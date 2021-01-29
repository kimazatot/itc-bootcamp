from rest_framework.serializers import ListSerializer, Serializer
import reservation
from .forms import ReservationForm
from reservation.models import Order
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import OrderSerializer
from reservation import serializers


def reserve(request):
    if request.method == 'POST':
        book_form = ReservationForm(request.POST)
        if book_form.is_valid():
            form = book_form.save(commit=False)
            form.reservator = User.objects.get(pk=request.user.pk)
            form.save()
            return redirect('reservation:my-reservations')
    else:
        book_form = ReservationForm()

    return render(
        request=request,
        template_name='reservation/reservation.html',
        context={"book_form": book_form}
    )


def display_reservations(request):
    user = User.objects.get(pk=request.user.pk)
    all_reservations = user.order_set.order_by('date')

    return render(
        request=request,
        template_name='reservation/orders.html',
        context={"user":user, "all_reservations": all_reservations}
    )


class ReservationListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        reservations = Order.objects.all()
        return reservations


class ReservationCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.OrderSerializer


    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "success": True,
                    "result": "Created Successfully!"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "success": False,
                "result": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class ReservationUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.OrderSerializer


    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "success": True,
                    "result": "Created Successfully!"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "success": False,
                "result": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class ReservationDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.OrderSerializer


    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "success": True,
                    "result": "Created Successfully!"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "success": False,
                "result": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )