import 'package:flutter/material.dart';
import 'option.dart';
import 'views/option_cell.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Travel App',
      theme: ThemeData(
        primarySwatch: Colors.cyan,
      ),
      home: Scaffold(
        appBar: AppBar(
            title: Text('Travel Recommender',
              style: TextStyle(
                color: Colors.white),
            )
        ),
        body: MyHomePage(),
      ),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return _myListView(context);
  }
}

Widget _myListView(BuildContext context) {

  final options = [
    new Option("Culture, Art and History.",
        "assets/images/culture_history_art.jpg",
        "history historical art architecture city culture"),
    new Option("Summer Vacation",
        "assets/images/beach_summer.jpg",
        "beach beaches park nature holiday sea seaside sand sunshine sun sunny"),
    new Option("Good Restaurants and Nightlife.",
        "assets/images/nightlife_fun_party.jpg",
        "nightclub nightclubs nightlife bar bars pub pubs party beer")
  ];

  return Column(
    children: <Widget>[
      Container(height: 8.0,),
      Text("Please let us know which one is more important for an ideal trip",
        textAlign: TextAlign.center,
        style: TextStyle(
          fontSize: 20.0,
          fontWeight: FontWeight.bold,
          color: Colors.cyan
        ),),
      Expanded(
        child: ListView.builder(
            itemCount: options.length,

            itemBuilder: (context, i) {
              return Card(
                elevation: 2.0,
                margin: EdgeInsets.all(16.0),
                child: FlatButton(
                  padding: EdgeInsets.all(0.0),
                  child: OptionCell(options[i]),
                  onPressed: () {
                    //TODO: Implement request.
                  },
                ),
              );
            }),
      )
    ],
  );
}

