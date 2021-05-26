import 'package:flutter/material.dart';
import 'dart:html' as htm;

extension MouseHover on Widget {
  static final mainContainer =
      htm.window.document.getElementById("mainContain");

  Widget onMouseHover({VoidCallback onEnter, VoidCallback onExit}) {
    return MouseRegion(
      onEnter: (_) {
        onEnter();
      },
      onHover: (_) {
        mainContainer.style.cursor = "pointer";
      },
      onExit: (_) {
        mainContainer.style.cursor = "default";
        onExit();
      },
      child: this,
    );
  }
}
