import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ..devices import DataFirmware, DataPreset, TPLinkExFirmware, TPLinkExPreset


TPLINK_EX_IP = "192.168.0.1"
DATA_DEVICE_IP = "192.168.101.1"


@require_GET
def index(request):
    return render(request, "index.html")


@require_POST
def update_firmware(request):
    try:
        TPLinkExFirmware.run_standalone()
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)


@require_POST
def use_preset(request):
    try:
        TPLinkExPreset.run_standalone()
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)


@require_POST
def data_update_firmware(request):
    try:
        DataFirmware.run_standalone()
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)


@require_POST
def data_use_preset(request):
    try:
        DataPreset.run_standalone()
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)
