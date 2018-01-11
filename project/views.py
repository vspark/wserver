from django.shortcuts import render

from datetime import datetime
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.


def admin_view(request):
    return render(request, 'project/admin.html')