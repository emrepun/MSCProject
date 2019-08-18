import 'package:flutter/material.dart';

class ReviewFeedbackPage extends StatelessWidget {

  final response;

  ReviewFeedbackPage(this.response);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        title: Text('Thanks!',
          style: TextStyle(
            color: Colors.white,
            //fontSize: 20.0
          ) ,),
      ),
      body: Center(
        child: Text(response,
          style: TextStyle(
              fontSize: 18.0,
              fontWeight: FontWeight.bold
          ),),
      ),
    );
  }
}