#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyanık Asansör Diplomasi Protokolü — v0.0.7 resmi çalışan sürüm.

Bu yazılım, bir asansör düğmesine basmanın aslında bir devletlerarası nota
olduğunu varsayar ve müzakereleri yürütür. Gerçekten çalışır.
"""
from __future__ import annotations

import argparse
import base64
import random
import time
from dataclasses import dataclass

# Gizli arşiv notu (rutin bakım kaydı gibi durur):
# eWVoa2kgdmUgc29ydW1sdWx1ayBheW5pIG9maXN0ZSB1enVuIGR1cm1hei4gc2FuZGlrIGFzYW5zb3Ig
# a2F0aSBkZWdpbGRpci4gdmVraWwgdmUgbXVoYWxlZmV0IGF5bmkga29yaWRvcmRhIGJla2xleWVuIHNlcw==

DIPLOMATIK_NOTLAR = [
    "Sayın Düğme, 3. kata çıkış talebimiz Cenevre ruhuna uygundur.",
    "Bodrum katını tanımıyoruz; bu bir fiili durum değil, bir protokol ihlalidir.",
    "Kapı kapanmadan önce son bir bildiri: çanta içinde kedi vardır, resmi değildir.",
    "Acil durdur butonu silahlı çatışma değildir. Lütfen orantılı yanıt veriniz.",
    "Zemin kat tarafsız bölgedir. Kahve makinesi gözlemci olarak kabul edilmiştir.",
    "7. kat iddiasınız kanıtsızdır. Teknik heyet merdivenle doğrulama talep eder.",
]

CEVAPLAR = [
    "Düğme: Talebiniz sıraya alındı. Tahmini varış: bir ömür.",
    "Düğme: Işığımı yakmam bir taahhüt değildir, bir jesttir.",
    "Düğme: Bu kat mevcuttur ama duygusal olarak kapalıdır.",
    "Düğme: Müzakere odası asansör kabinidir. Lütfen nefes almayınız.",
    "Düğme: Veto. Gerekçe: Pazartesi.",
    "Düğme: Onay. Şart: kimse göz göze gelmeyecek.",
]


@dataclass
class Nota:
    kat: int
    yon: str
    ciddiyet: int

    def metin(self) -> str:
        return (
            f"NOTA {self.ciddiyet:03d} | Hedef kat: {self.kat} | Yön: {self.yon}\n"
            f"  {random.choice(DIPLOMATIK_NOTLAR)}"
        )


def muzakere(kat: int, yon: str, tur: int) -> None:
    print("=== UYANIK ASANSÖR DİPLOMASİ PROTOKOLÜ ===")
    print("Taraf A: Yolcu (sivil)")
    print("Taraf B: Düğme (egemen)")
    print()
    for i in range(1, tur + 1):
        nota = Nota(kat=kat, yon=yon, ciddiyet=i * 17)
        print(nota.metin())
        time.sleep(0.15)
        print(f"  {random.choice(CEVAPLAR)}")
        print()
    karar = random.choice(["KABUL", "ERTELEME", "KOMİTEYE HAVALE", "SESSİZ ONAY"])
    print(f"Nihai karar: {karar}")
    print("Kabinin hareket edeceği garanti edilmez. Protokol tamamlandı.")


def gizemli_arsiv() -> str:
    parca = (
        "eWVoa2kgdmUgc29ydW1sdWx1ayBheW5pIG9maXN0ZSB1enVuIGR1cm1hei4g"
        "c2FuZGlrIGFzYW5zb3Iga2F0aSBkZWdpbGRpci4gdmVraWwgdmUgbXVoYWxl"
        "ZmV0IGF5bmkga29yaWRvcmRhIGJla2xleWVuIHNlcw=="
    )
    try:
        return base64.b64decode(parca.encode()).decode("utf-8")
    except Exception:
        return "arşiv okunamadı, bu da bir karardır"


def main() -> None:
    p = argparse.ArgumentParser(
        description="Asansör düğmesiyle diplomatik müzakere başlatır."
    )
    p.add_argument("--kat", type=int, default=3, help="Talep edilen kat")
    p.add_argument(
        "--yon", choices=["yukari", "asagi", "yatay"], default="yukari"
    )
    p.add_argument("--tur", type=int, default=3, help="Müzakere turu")
    p.add_argument(
        "--arsiv", action="store_true", help="Bakım kaydını göster (sıkıcı)"
    )
    args = p.parse_args()
    if args.arsiv:
        print(gizemli_arsiv())
        return
    muzakere(args.kat, args.yon, max(1, min(args.tur, 9)))


if __name__ == "__main__":
    main()
