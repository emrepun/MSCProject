import 'package:flutter/material.dart';

class RecommendationPage extends StatelessWidget {

  final cities;

  RecommendationPage(this.cities);

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      backgroundColor: Colors.cyan,
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        title: Text('Recommendations based on your preferences'),
      ),
      body: Text('Sample'),
    );
  }
}
