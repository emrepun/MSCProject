import 'package:flutter/material.dart';
import 'views/city_cell.dart';

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
      body: ListView.builder(
          itemCount: cities.length,
          itemBuilder: (context, i) {
            return Card(
              elevation: 2.0,
              margin: EdgeInsets.all(16.0),
              child: FlatButton(
                padding: EdgeInsets.all(0.0),
                child: CityCell(cities[i]),
                onPressed: () {
                  //TODO: Implement selection of the recommended city.
                },
              ),
            );
          })
    );
  }
}
