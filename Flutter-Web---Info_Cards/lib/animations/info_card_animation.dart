import 'package:flutter/material.dart';
import 'package:info_cards/models/info_models.dart';
import 'package:info_cards/extensions/mouse_hover.dart';

class InfoCardAnimation extends StatefulWidget {
  final InfoModel info;

  InfoCardAnimation({this.info});

  @override
  _InfoCardAnimationState createState() => _InfoCardAnimationState();
}

class _InfoCardAnimationState extends State<InfoCardAnimation>
    with SingleTickerProviderStateMixin {
  var info = InfoModel.list.elementAt(0);
  AnimationController animationController;
  Animation<Color> animationColor;
  Animation<Color> animationIconColor;
  Animation<double> animPosnout;
  Animation<double> animOpacityOut;
  Animation<double> animPosnIn;
  Animation<double> animOpacityIn;

  @override
  void initState() {
    animationController =
        AnimationController(vsync: this, duration: Duration(milliseconds: 250));
    animationColor = ColorTween(begin: Colors.cyan, end: Colors.blueGrey)
        .animate(animationController)
          ..addListener(() {
            setState(() {});
          });
    animationIconColor = ColorTween(begin: Colors.blueAccent, end: Colors.white)
        .animate(animationController)
          ..addListener(() {
            setState(() {});
          });

    animPosnIn = Tween(begin: 0.0, end: 5.0).animate(
        CurvedAnimation(parent: animationController, curve: Interval(.5, 1.0)))
      ..addListener(() {
        setState(() {});
      });

    animOpacityIn = Tween(begin: 0.0, end: 1.0).animate(
        CurvedAnimation(parent: animationController, curve: Interval(.5, 1.0)))
      ..addListener(() {
        setState(() {});
      });
    super.initState();

    animPosnout = Tween(begin: 130.0, end: 140.0).animate(
        CurvedAnimation(parent: animationController, curve: Interval(0.0, .5)))
      ..addListener(() {
        setState(() {});
      });

    animOpacityOut = Tween(begin: 1.0, end: 0.0).animate(
        CurvedAnimation(parent: animationController, curve: Interval(0.0, .5)))
      ..addListener(() {
        setState(() {});
      });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      color: animationColor.value,
      child: Container(
        width: 400,
        height: 300,
        child: Stack(
          children: [
            Positioned(
              right: 200 - (10.0 - animPosnIn.value),
              child: Icon(
                Icons.wifi,
                size: 300,
                color: Colors.white24,
              ),
            ),
            Container(
              width: 400,
              height: 300,
              padding: EdgeInsets.all(16),
              child: Column(
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Icon(
                        Icons.wifi,
                        size: 52,
                        color: animationIconColor.value,
                      ),
                      Expanded(child: SizedBox()),
                      Opacity(
                        opacity: animOpacityIn.value,
                        child: IconButton(
                            icon: Icon(
                              Icons.arrow_forward_ios_rounded,
                              size: 35,
                              color: Colors.white,
                            ),
                            onPressed: null),
                      ),
                      SizedBox(
                        width: 5.0 - animPosnIn.value,
                      ),
                    ],
                  ),
                  SizedBox(
                    height: 10 + animPosnIn.value,
                  ),
                  Opacity(
                    opacity: animOpacityIn.value,
                    child: Text(
                      info.description,
                      style: TextStyle(
                          fontSize: 17, color: Colors.white, height: 1.5),
                    ),
                  ),
                ],
              ),
            ),
            Positioned(
                top: animPosnout.value,
                child: Opacity(
                  opacity: animOpacityOut.value,
                  child: Container(
                    width: 400,
                    height: 170,
                    padding: EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          info.title,
                          style: TextStyle(fontSize: 28, color: Colors.black87),
                        ),
                        Container(
                          height: 1,
                          width: double.infinity,
                          color: Colors.black26,
                          margin: EdgeInsets.symmetric(vertical: 12),
                        ),
                        Text(info.subtitle,
                            style:
                                TextStyle(fontSize: 14, color: Colors.black38))
                      ],
                    ),
                  ),
                ))
          ],
        ),
      ),
    ).onMouseHover(
      onEnter: () {
        animationController.forward();
      },
      onExit: () {
        animationController.reverse();
      },
    );

    // throw UnimplementedError();
  }
}
