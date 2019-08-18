import 'package:flutter/material.dart';
//import 'package:travel_app2/city.dart';
import 'package:travel_app2/review_compose_page.dart';


class DestinationPage extends StatelessWidget {

  final city;

  DestinationPage(this.city);

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        title: Text(city.title,
          style: TextStyle(
            color: Colors.white,
            //fontSize: 20.0
          ) ,),
      ),
      //TODO: Implement body.
      body: Column(
        children: <Widget>[
          Image.network(city.imageUrl),
          Container(height: 8.0,),
          Text(city.popularity,
            style: TextStyle(
                color: Colors.black54,
                fontWeight: FontWeight.bold,
                fontSize: 12.0)),
          Container(height: 16.0,),
          Padding(
            padding: EdgeInsets.all(12.0),
            child: Text(city.description,
              style: TextStyle(
                  color: Colors.black,
                  fontSize: 16.0
              ),),
          ),
          Card(
            elevation: 2.0,
            margin: EdgeInsets.all(32.0),
            child: Container(
              color: Colors.cyan,
              child: FlatButton(
                padding: EdgeInsets.all(16.0),
                child: Text("Write a review",
                  style: TextStyle(color: Colors.white),),
                onPressed: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(builder: (context) {
                      return ReviewComposePage();
                    })
                  );
                  //TODO: Implement fetching interesting places.
                },
              ),
            ),
          )
        ],
      ),
    );
  }
}