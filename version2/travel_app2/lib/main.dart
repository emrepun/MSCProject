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
    new Option("first", "firstImage", "first keywords"),
    new Option("second", "secondImage", "second keywords"),
    new Option("third", "thirdImage", "third keywords")
  ];

  return ListView.builder(
    itemCount: options.length,
    itemBuilder: (context, index) {
      return Card(
        elevation: 2.0, //gives some kind of shadow at the end.
        margin: EdgeInsets.all(20.0),
        child: ListTile(
          //leading: Icon(icons[index]),
          title: Text(options[index].title),
        ),
      );
    },
  );
}

