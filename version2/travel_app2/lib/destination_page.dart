import 'package:flutter/material.dart';
import 'package:travel_app2/city.dart';


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
    );
  }

}