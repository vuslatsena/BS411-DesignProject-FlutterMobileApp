import 'package:flutter/material.dart';
import '../global.dart';
//bu sayfada ıntray yazılı alanın widget yapısı oluşturuluyor

class IntrayTodo extends StatelessWidget {
  final String title;
  final String keyValue;
  IntrayTodo({this.keyValue, this.title});

  @override
  Widget build(BuildContext context) {
    return Container(
      key: Key(keyValue),
      margin: EdgeInsets.only(bottom: 5),
      padding: EdgeInsets.all(10),
      height: 100,
      decoration: BoxDecoration(
        color: redColor,
        borderRadius: BorderRadius.all(Radius.circular(10)),
        boxShadow: [
          new BoxShadow(
            color: Colors.black.withOpacity(0.5),
            blurRadius: 10.0,
          ),
        ],
      ),
      child: Row(
        children: <Widget>[
          // ignore: missing_required_param
          Radio(),
          Column(
            children: <Widget>[
              Text(
                title,
                style: darkTodoTitle,
              )
            ],
          )
        ],
      ),
    );
  }
}

/*Sources 
https://medium.com/flutter-community/create-a-draggable-widget-in-flutter-50b61f12635d 
https://api.flutter.dev/flutter/material/ReorderableListView-class.html
*/
