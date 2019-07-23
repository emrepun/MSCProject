import 'package:flutter/material.dart';

class RecommendationPage extends StatelessWidget {

  final cities;

  RecommendationPage(this.cities);

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        title: Text('Recommended Destinations',
          style: TextStyle(
            color: Colors.white,
            //fontSize: 20.0
          ) ,),
      ),
      body: Text('Sample'),
    );
  }
}
