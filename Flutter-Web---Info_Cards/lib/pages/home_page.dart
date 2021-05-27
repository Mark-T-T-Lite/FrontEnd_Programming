import 'package:flutter/material.dart';
import '../animations/info_card_animation.dart';
import 'package:info_cards/models/info_models.dart';

class HomePage extends StatefulWidget {
  @override
  _InfoPageState createState() => _InfoPageState();
}

class _InfoPageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black45,
      body: Center(
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            InfoCardAnimation(info: InfoModel.list.elementAt(1)),
            SizedBox(width: 25),
            InfoCardAnimation(
              info: InfoModel.list.elementAt(0),
            ),
          ],
        ),
      ),
    );
    // throw UnimplementedError();
  }
}
