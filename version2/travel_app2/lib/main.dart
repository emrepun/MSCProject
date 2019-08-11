import 'package:flutter/material.dart';
import 'option.dart';
import 'views/option_cell.dart';
import 'dart:convert';
import 'dart:io';
import 'city.dart';
import 'recommendation_page.dart';

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
    new Option("Beach and Sun",
        "assets/images/beach_summer.jpg",
        "beach beaches park nature holiday sea seaside sand sunshine sun sunny"),
    new Option("Nightlife and Party.",
        "assets/images/nightlife_fun_party.jpg",
        "nightclub nightclubs nightlife bar bars pub pubs party beer")
  ];

  void postOption({Map body}) async {
    final url = 'http://localhost:5000/api';
    HttpClient httpClient = new HttpClient();
    HttpClientRequest request = await httpClient.postUrl(Uri.parse(url));
    request.add(utf8.encode(json.encode(body)));
    HttpClientResponse response = await request.close();

    String reply = await response.transform(utf8.decoder).join();

    final cities = (json.decode(reply) as List).map((i) {
      final title = i['city'];
      final description = i['description'];
      final popularity = i['popularity'];
      final imageUrl = i['image'];

      return new City(title, description, popularity, imageUrl);
    }).toList();

    print(cities[0]);

    Navigator.of(context).push(
      MaterialPageRoute(builder: (context) {
        return RecommendationPage(cities);
      })
    );
  }

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
                    final body = options[i].optionToJson(true);
                    postOption(body: body);
                  },
                ),
              );
            }),
      )
    ],
  );
}

