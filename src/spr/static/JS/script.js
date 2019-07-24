function add() {

	//Create an input type dynamically.
	var list = document.createElement("LI");
	var milestone = document.createElement("INPUT");

	var array = ["Incomplete", "In Progress", "Completed"];
	var status = document.createElement("SELECT");

	for (var i = 0; i < array.length; i++) {
		var option = document.createElement("option");
		option.value = array[i];
		option.text = array[i];
		status.append(option);
	}

	//Assign different attributes to the element.
	milestone.setAttribute("type", "text");
	milestone.setAttribute("value", "");
	milestone.setAttribute("name", "milestone");

	list.appendChild(milestone);
	list.appendChild(status);

	// 'addMilestone' is the div id, where new fields are to be added
	var add_milestone = document.getElementById("addMilestone");

	//Append the element in page (in span).
	add_milestone.appendChild(list);
}

// function parse() {
// 	var milestone_list = milestone_var.split(',');
// 	var milestone = document.getElementById('milestone')
// 	for (var i = 0; i < milestone_list.length; i++) {
// 		var list = document.createElement("LI");
// 		var textnode = document.createTextNode(milestone_list[i]);
// 		list.appendChild(textnode);
// 		milestone.appendChild(list);
// 	}
// }