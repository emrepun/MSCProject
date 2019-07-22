import 'package:flutter/material.dart';
import 'option.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Travel App',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: Scaffold(
        appBar: AppBar(title: Text('Travel Recommender')),
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
    new Option("first", "assets/images/culture_history_art.jpg", "first keywords"),
    new Option("second", "assets/images/beach_summer.jpg", "second keywords"),
    new Option("third", "assets/images/nightlife_fun_party.jpg", "third keywords")
  ];


  return Center(
    child: ListView.builder(
        itemCount: options.length,

        itemBuilder: (context, i) {
          return Card(
            elevation: 2.0,
            margin: EdgeInsets.all(16.0),
            child: FlatButton(
              padding: EdgeInsets.all(0.0),
              child: Column(
                children: <Widget>[
                  new Container(
                    padding: EdgeInsets.all(2.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Image.asset(options[i].imageName),
                        Container(height: 8.0,),
                        Text(options[i].title,
                          style: TextStyle(
                            fontSize: 16.0,
                            fontWeight: FontWeight.bold
                          ),)
                      ],
                    ),
                  )
                ],
              ),
              onPressed: () {
                //TODO: Implement request.
              },
            ),
          );
        }),
  );
}

