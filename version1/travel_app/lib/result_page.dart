import 'package:flutter/material.dart';

import 'data_model.dart';

class ResultPage extends StatefulWidget {
  final int city;

  ResultPage(this.city);

  @override
  _ResultPageState createState() => _ResultPageState();

}

class _ResultPageState extends State<ResultPage> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    String cityName = '';
    String backgroundImage = 'assets/images/istanbul.jpg';
    if (widget.city == 0) {
      cityName = 'Istanbul';
      backgroundImage = 'assets/images/istanbul.jpg';
    } else if (widget.city == 1) {
      cityName = 'London';
      backgroundImage = 'assets/images/london.jpg';
    } else if (widget.city == 2) {
      cityName = 'Prague';
      backgroundImage = 'assets/images/prague.jpg';
    } else if (widget.city == 3) {
      cityName = 'Amsterdam';
      backgroundImage = 'assets/images/amsterdam.jpg';
    } else if (widget.city == 4) {
      cityName = 'Antalya';
      backgroundImage = 'assets/images/antalya.jpg';
    } else if (widget.city == 5) {
      cityName = 'Dubrovnik';
      backgroundImage = 'assets/images/dubrovnik.jpg';
    } else if (widget.city == 6) {
      cityName = 'Ibiza';
      backgroundImage = 'assets/images/ibiza.jpg';
    } else if (widget.city == 7) {
      cityName = 'Hvar';
      backgroundImage = 'assets/images/hvar.jpg';
    } else if (widget.city == 8) {
      cityName = 'Verbier';
      backgroundImage = 'assets/images/verbier.jpg';
    } else if (widget.city == 9) {
      cityName = 'Vogel';
      backgroundImage = 'assets/images/vogel.jpg';
    } else if (widget.city == 10) {
      cityName = 'Bangkok';
      backgroundImage = 'assets/images/bangkok.jpg';
    } else if (widget.city == 11) {
      cityName = 'Sao Paulo';
      backgroundImage = 'assets/images/saopaulo.jpg';
    } else {
      cityName = ' ';
    }
    return Scaffold(
      backgroundColor: Colors.cyan,
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        title: Text('Your destination is: $cityName'),
      ),
      //body: Image.asset(backgroundImage),
      body: Column(
        children: <Widget>[
          Image.asset(backgroundImage),
          Padding(padding: EdgeInsets.all(16.0),),
          Text('Are you ready to explore $cityName?',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 24.0,
          color: Colors.white),),
          Padding(padding: EdgeInsets.all(16.0),),
          RaisedButton(
            onPressed: () => print('begin pressed.'),
            color: Colors.white,
            child: Text('Lets Begin!',
            style: TextStyle(color: Colors.cyan,
            fontSize: 20.0),),
          )
        ],
      ),
    );
  }
}