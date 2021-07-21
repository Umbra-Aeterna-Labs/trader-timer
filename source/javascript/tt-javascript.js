import moment from 'moment';

let hrs_left = Integer(window.prompt("Enter the # of hours remaining on trader:"));
let date_end = moment().add(hrs_left, 'h').format("ddd MMM Do YYYY at h:m a");
console.log(date_end);
