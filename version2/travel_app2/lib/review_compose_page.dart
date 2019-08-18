import 'package:flutter/material.dart';

class ReviewComposePage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.cyan,
          title: Text('Write a review',
            style: TextStyle(
              color: Colors.white,
              //fontSize: 20.0
            ) ,),
      ),
      body: Column(
        children: <Widget>[
          Container(
            height: 600,
            child: Padding(
              padding: EdgeInsets.all(16.0),
              child: TextField(
                maxLines: null,
                style: TextStyle(
                  fontSize: 18.0,
                  color: Colors.black,
                ),
              ),
            )
          ),
          Column(
            children: <Widget>[
              Container(height: 100,),
              Container(
                color: Colors.cyan,
                child: FlatButton(
                  padding: EdgeInsets.all(16.0),
                  child: Text("Submit Review",
                    style: TextStyle(color: Colors.white),),
                  onPressed: () {
                    print("Review Submitted.");
                  },
                ),
              )
            ],
          ),
        ],
      ),
    );
  }
}