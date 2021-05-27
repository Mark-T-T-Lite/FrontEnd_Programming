import 'package:flutter/material.dart';

class InfoModel {
  final int id;
  final String title;
  final Icon icon;
  final String subtitle;
  final String description;

  InfoModel({this.id, this.title, this.icon, this.subtitle, this.description});

  static List<InfoModel> list = [
    InfoModel(
        id: 1,
        title: "T_Lite",
        icon: Icon(
          Icons.wifi,
          size: 52,
          // color: InfoCardAnimation.animationIconColor.value,
        ),
        subtitle: "Fast Speeds and High BandWidth\nSlow Wi-Fi Solution ",
        description:
            "Have a zoom lecture to attend?\nIs the connection unstable? Do wanna download quickly? T_Lite is a Fast Speeds and High BandWidth AP that can help you\n\n\n\nGet access to T_Lite Now"),
    InfoModel(
      id: 2,
      title: "Never Be Like You",
/*       icon: "Flume - Kai",
 */
      subtitle: "60",
    ),
    /*InfoModel(
      id: 3,
      title: "Lose It",
      icon: "Flume - Vic Mensa",
      subtitle: 60,
    ),
    InfoModel(
      id: 4,
      title: "Numb & Getting Colder",
      icon: "Flume - KUCKA",
      subtitle: 60,
    ),
    InfoModel(
      id: 5,
      title: "Say It",
      icon: "Flume - Tove Lo",
      subtitle: 60,
    ),
    InfoModel(
      id: 6,
      title: "Wall F*ck",
      icon: "Flume",
      subtitle: 60,
    ),
    InfoModel(
      id: 7,
      title: "Pika",
      icon: "Flume",
      subtitle: 60,
    ) */
  ];
}
