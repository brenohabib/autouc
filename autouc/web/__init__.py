import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ..devices import TPLinkExFirmware, TPLinkExPreset, DataFirmware, DataPreset


DEVICE_IP = "192.168.0.1"


def ping_device(ip: str) -> bool:
    param = '-n' if os.name == 'nt' else '-c'
    hostname = ip
    try:
        response = os.system(f"ping {param} 1 {hostname}")
        print(f"Ping {hostname} returned {response}")
        return response == 0
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


@require_POST
def data_update_firmware(request):
    from playwright.sync_api import sync_playwright

    try:
        with sync_playwright() as playwright:
            DataFirmware.run(playwright)
        return JsonResponse({"ok": True})
    except Exception:
        return JsonResponse({"ok": False}, status=500)


@require_POST
def data_use_preset(request):
    from playwright.sync_api import sync_playwright

    try:
        with sync_playwright() as playwright:
            DataPreset.run(playwright)
        return JsonResponse({"ok": True})
    except Exception:
        return JsonResponse({"ok": False}, status=500)
