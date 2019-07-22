class Option {
  final title;
  final imageName;
  final keywords;

  //constructor.
  Option(this.title, this.imageName, this.keywords);

  Map<String, dynamic> optionToJson(bool isKeywordOnly) {
    if (isKeywordOnly) {
      return <String, dynamic> {'keywords': this.keywords};
    } else {
      return <String, dynamic> {
        'title': this.title,
        'imageName': this.imageName,
        'keywords': this.keywords};
    }
  }
}