import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:io';
import 'package:travel_app2/review_feedback.dart';

class ReviewComposePage extends StatelessWidget {

  TextEditingController reviewController = TextEditingController();

  void postReview(review, context) async {
    final body = <String, dynamic> {'review': review};
    final url = 'http://localhost:5000/api/submit_review';
    HttpClient httpClient = new HttpClient();
    HttpClientRequest request = await httpClient.postUrl(Uri.parse(url));
    request.add(utf8.encode(json.encode(body)));
    HttpClientResponse response = await request.close();

    String reply = await response.transform(utf8.decoder).join();

    final outcome = json.decode(reply)['outcome'];
    print(outcome);

    var feedback = '';

    if (outcome == 1) {
      feedback = 'Your feedback was positive!';
    } else {
      feedback = 'Your feedback was negative!';
    }

    Navigator.of(context).push(
      MaterialPageRoute(builder: (context) {
        return ReviewFeedbackPage(feedback);
      })
    );
  }

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
                controller: reviewController,
                onChanged: (v) => reviewController.text = v,
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
                    postReview(reviewController.text, context);
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