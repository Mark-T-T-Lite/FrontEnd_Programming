import 'package:flutter/material.dart';
import 'Fade.dart';

var imagesDict = {
  1: "/images/one.jpg",
  2: "/images/two.jpg",
  3: "Japanese Ryokan",
  4: "Serviced Apartment",
  5: "Ryokan (旅館)[a] is a type of traditional Japanese inn that typically features tatami-matted rooms, communal baths, and other public areas where visitors may wear yukata and talk with the owner",
  6: " Photograph courtesy of MORI LIVING - luxurious residences for lease and residences for sale.It stands for a totally new Tokyo lifestyle, in residences that exceed all previous expectations for life in Tokyo or Japan"
};
void main() {
  runApp(ToursRentalsApp());
}

class ToursRentalsApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tours and Rentals',
      theme: ThemeData(),
      home: RentalsPage(title: 'Rentals'),
    );
  }
}

class RentalsPage extends StatefulWidget {
  RentalsPage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _RentalsPageState createState() => _RentalsPageState();
}

class _RentalsPageState extends State<RentalsPage>
    with TickerProviderStateMixin {
  var _scrollController, _tabController, _tabController2;
  PageController _pageController;

  @override
  void initState() {
    _scrollController = ScrollController();
    _tabController = TabController(vsync: this, length: 2);
    _tabController2 = TabController(vsync: this, length: 2);

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: NestedScrollView(
        controller: _scrollController,
        headerSliverBuilder: (BuildContext context, bool innerBoxIsScrolled) {
          return <Widget>[
            SliverAppBar(
              title: Text(widget.title),
              pinned: true,
              floating: true,
              snap: false,
              forceElevated: innerBoxIsScrolled,
              backgroundColor: Colors.black,
              bottom: TabBar(
                tabs: <Tab>[
                  Tab(text: "Inn"),
                  Tab(text: "Apartments"),
                ],
                controller: _tabController,
              ),
            ),
          ];
        },
        body: TabBarView(
          controller: _tabController,
          children: <Widget>[
            _pageView(1),
            _pageView(2),
          ],
        ),
      ),
    );
  }

  _pageView(var imageCount) {
    return Container(
        child: PageView(
      controller: _pageController,
      children: <Widget>[
        makePage(
            page: imageCount,
            image: imagesDict[imageCount],
            title: imagesDict[imageCount + 2],
            description: imagesDict[imageCount + 4]),
        review(controller: _tabController2)
      ],
      scrollDirection: Axis.vertical,
    ));
  }
}

Widget makePage({image, title, description, page}) {
  int totalPage = 2;
  return Container(
    decoration: BoxDecoration(
        image:
            DecorationImage(image: AssetImage(image), fit: BoxFit.fitHeight)),
    child: Container(
      decoration: BoxDecoration(
          gradient: LinearGradient(begin: Alignment.bottomRight, stops: [
        0.3,
        0.9
      ], colors: [
        Colors.black.withOpacity(.9),
        Colors.black.withOpacity(.2),
      ])),
      child: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              SizedBox(
                height: 40,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                crossAxisAlignment: CrossAxisAlignment.baseline,
                textBaseline: TextBaseline.alphabetic,
                children: <Widget>[
                  FadeAnimation(
                      2,
                      Text(
                        page.toString(),
                        style: TextStyle(
                            color: Colors.white,
                            fontSize: 30,
                            fontWeight: FontWeight.bold),
                      )),
                  Text(
                    '/' + totalPage.toString(),
                    style: TextStyle(color: Colors.white, fontSize: 15),
                  )
                ],
              ),
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    FadeAnimation(
                        1,
                        Text(
                          title,
                          style: TextStyle(
                              color: Colors.white,
                              fontSize: 50,
                              height: 1.2,
                              fontWeight: FontWeight.bold),
                        )),
                    SizedBox(
                      height: 20,
                    ),
                    FadeAnimation(
                        1.5,
                        Row(
                          children: <Widget>[
                            Container(
                              margin: EdgeInsets.only(right: 3),
                              child: Icon(
                                Icons.star,
                                color: Colors.yellow,
                                size: 15,
                              ),
                            ),
                            Container(
                              margin: EdgeInsets.only(right: 3),
                              child: Icon(
                                Icons.star,
                                color: Colors.yellow,
                                size: 15,
                              ),
                            ),
                            Container(
                              margin: EdgeInsets.only(right: 3),
                              child: Icon(
                                Icons.star,
                                color: Colors.yellow,
                                size: 15,
                              ),
                            ),
                            Container(
                              margin: EdgeInsets.only(right: 3),
                              child: Icon(
                                Icons.star,
                                color: Colors.yellow,
                                size: 15,
                              ),
                            ),
                            Container(
                              margin: EdgeInsets.only(right: 5),
                              child: Icon(
                                Icons.star,
                                color: Colors.grey,
                                size: 15,
                              ),
                            ),
                            Text(
                              '4.0',
                              style: TextStyle(color: Colors.white70),
                            ),
                            Text(
                              '(2300)',
                              style: TextStyle(
                                  color: Colors.white38, fontSize: 12),
                            )
                          ],
                        )),
                    SizedBox(
                      height: 20,
                    ),
                    FadeAnimation(
                        2,
                        Padding(
                          padding: const EdgeInsets.only(right: 50),
                          child: Text(
                            description,
                            style: TextStyle(
                                color: Colors.white.withOpacity(.7),
                                height: 1.9,
                                fontSize: 15),
                          ),
                        )),
                    SizedBox(
                      height: 20,
                    ),
                    FadeAnimation(
                        2.5,
                        Text(
                          'SLIDE UP',
                          style: TextStyle(color: Colors.white),
                        )),
                    SizedBox(
                      height: 30,
                    ),
                  ],
                ),
              )
            ]),
      ),
    ),
  );
}

Widget review({controller}) {
  return Container(
      child: TabBarView(
    controller: controller,
    children: <Widget>[
      _descriptionView(),
      _nearbyReview(),
    ],
  ));
}

Widget _nearbyReview() {
  return CustomScrollView(
    slivers: <Widget>[
      SliverFixedExtentList(
        itemExtent: 50.0,
        delegate: SliverChildBuilderDelegate(
          (BuildContext context, int index) {
            return Container(
              alignment: Alignment.center,
              color: Colors.lightBlue[100 * (index % 9)],
              child: Text('List Item $index'),
            );
          },
        ),
      ),
    ],
  );
}

Widget _descriptionView() {
  return Text("DESCRIPTION HERE");
}
