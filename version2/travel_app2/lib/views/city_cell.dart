import 'package:flutter/material.dart';
import 'package:travel_app2/city.dart';

class CityCell extends StatelessWidget {

  final city;

  CityCell(this.city);

  @override
  Widget build(BuildContext context) {
    return new Column(
      children: <Widget>[
        new Container(
          padding: EdgeInsets.all(2.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Image.network(city.imageUrl),
              Container(height: 8.0,),
              Text(city.title,
                style: TextStyle(
                    fontSize: 16.0,
                    fontWeight: FontWeight.bold
                ),),
              Text(city.popularity,
                style: TextStyle(
                  fontSize: 12.0,
                ),)
            ],
          ),
        )
      ],
    );
  }
}