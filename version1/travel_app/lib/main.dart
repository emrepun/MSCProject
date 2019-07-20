import 'package:flutter/material.dart';
import 'data_model.dart';
import 'dart:convert';
import 'dart:io';
import 'dart:async';
import 'result_page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController ageController = TextEditingController();
  TextEditingController budgetController = TextEditingController();
  TextEditingController seasonController = TextEditingController();

  // You'll need the context in order for the Navigator to work.
  void submitData(BuildContext context) {
    var newData = Data(int.parse(ageController.text),
      int.parse(budgetController.text),
      seasonController.text
    );

    postData('http://localhost:5000/api', body: newData.toJson());
    print('lows');
  }

  void postData(String url, {Map body}) async {
    HttpClient httpClient = new HttpClient();
    HttpClientRequest request = await httpClient.postUrl(Uri.parse(url));
    request.add(utf8.encode(json.encode(body)));
    HttpClientResponse response = await request.close();

    String reply = await response.transform(utf8.decoder).join();
    int city = json.decode(reply)['city'];
    httpClient.close();
    print(city);
    Navigator.of(context).push(
      MaterialPageRoute(builder: (context) {
        return ResultPage(city);
      },)
    );
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(
        title: Text('Travel Guide'),
        backgroundColor: Colors.cyan,
      ),
      body: Container(
        color: Colors.white70,
        child: Padding(
          padding: const EdgeInsets.symmetric(
            vertical: 8.0,
            horizontal: 32.0,
          ),
          child: Column(
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.only(bottom: 8.0),
                child: TextField(
                  controller: ageController,
                  onChanged: (v) => ageController.text = v,
                  decoration: InputDecoration(
                    labelText: 'Your age',
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(bottom: 8.0),
                child: TextField(
                  controller: budgetController,
                  onChanged: (v) => budgetController.text = v,
                  decoration: InputDecoration(
                    labelText: "Your budget (500 - 5000) \$",
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(bottom: 8.0),
                child: TextField(
                  controller: seasonController,
                  onChanged: (v) => seasonController.text = v,
                  decoration: InputDecoration(
                    labelText: 'Season you want to travel',
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Builder(
                    builder: (context) {
                      return RaisedButton(
                        onPressed: () => submitData(context),
                        color: Colors.indigoAccent,
                        child: Text('Lets travel!'),
                      );
                    }
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
