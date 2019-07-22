import 'package:flutter/material.dart';

class OptionCell extends StatelessWidget {

  final option;

  OptionCell(this.option);

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return new Column(
      children: <Widget>[
        new Container(
          padding: EdgeInsets.all(2.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Image.asset(option.imageName),
              Container(height: 8.0,),
              Text(option.title,
                style: TextStyle(
                    fontSize: 16.0,
                    fontWeight: FontWeight.bold
                ),)
            ],
          ),
        )
      ],
    );
  }
}