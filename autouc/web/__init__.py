import platform
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ..devices import TPLinkExFirmware, TPLinkExPreset


DEVICE_IP = "192.168.0.1"


def ping_device(ip: str) -> bool:
    system = platform.system().lower()
    count_param = "-n" if system == "windows" else "-c"
    command = ["ping", count_param, "1", ip]
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False


@require_GET
def index(request):
    return render(request, "index.html")


@require_GET
def device_status(request):
    online = ping_device(DEVICE_IP)
    status = "ONLINE" if online else "OFFLINE"
    return JsonResponse({"status": status})


@require_POST
def update_firmware(request):
    from playwright.sync_api import sync_playwright

    try:
        with sync_playwright() as playwright:
            TPLinkExFirmware.run(playwright)
        return JsonResponse({"ok": True})
    except Exception:
        return JsonResponse({"ok": False}, status=500)


@require_POST
def use_preset(request):
    from playwright.sync_api import sync_playwright

    try:
        with sync_playwright() as playwright:
            TPLinkExPreset.run(playwright)
        return JsonResponse({"ok": True})
    except Exception:
        return JsonResponse({"ok": False}, status=500)
