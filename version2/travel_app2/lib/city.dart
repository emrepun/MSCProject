class City {
  final title;
  final description;
  final popularity;
  final imageUrl;

  City(this.title, this.description, this.popularity, this.imageUrl);

  @override
  String toString() {
    return "Name: " + this.title + "\nDescription: " + this.description + "\nReview Count: " + this.popularity + "\nImage Url. " + this.imageUrl;
  }
}