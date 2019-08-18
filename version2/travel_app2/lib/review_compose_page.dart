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
    );
  }
}