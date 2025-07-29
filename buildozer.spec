[app]
title = Online Clicker
package.name = onlineclicker
package.domain = org.example
source.dir = .
version = 1.0
entrypoint = main.py
source.include_exts = py,png,kv,atlas
requirements = python3,kivy==2.3.0,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.meta_data = {'android.hardware.opengles.aep': 'true'}

android.minapi = 21
android.api = 34
android.archs = armeabi-v7a
android.debug = 0
android.release_artifact = apk
android.ndk = 23b

android.accept_sdk_license = True

[buildozer]
warn_on_root = 1
log_level = 2
