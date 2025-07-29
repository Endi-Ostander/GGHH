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
fullscreen = 0
android.permissions = INTERNET

android.minapi = 33
android.api = 34
android.archs = armeabi-v7a
android.debug = 0
android.release_artifact = apk
android.ndk = 25b

log_level = 2
android.accept_sdk_license = True
