from django.contrib import admin
from .models import *


admin.site.register(Player)
admin.site.register(MotionRecognition)
admin.site.register(Round)
admin.site.register(PoseEstimation)
admin.site.register(Point)