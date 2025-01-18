/*! {% load static %} */

let state = JSON.parse('{{GAME_STATE}}'.replaceAll('&quot;', '"'));
let [names0, names1] = state['names'];
let [team0, team1] = state['game'];
let [stats0, stats1] = state['stats'];
let problems = state['problems'];


let table0 = document.getElementById('team0');
let table1 = document.getElementById('team1');

let cellText = {'0': '', '1': '•', '2': 'X', '3': '⚰️'};

function draw_table(id, table, state, names) {
    {
        let tr = document.createElement('tr');
        let th = document.createElement('th');
        th.classList.add('name');
        th.classList.add('problem');
        th.innerText = `Корабли команды ${id + 1}`
        tr.append(th);
        for (let i = 0; i < problems.length; ++i) {
            let th = document.createElement('th');
            th.classList.add('problem');
            th.innerText = problems[i];
            tr.append(th);
        }
        table.append(tr)
    }
    for (let i = 0; i < state.length; ++i) {
        let line = state[i];
        let tr = document.createElement('tr');
        let th = document.createElement('th');
        th.classList.add('name')
        th.innerText = names[i];
        tr.append(th);
        for (let el of line) {
            let td = document.createElement('td');
            td.classList.add('s' + el);
            td.innerText = cellText[el];
            tr.append(td);
        }
        table.append(tr)
    }
}

function draw_stats(id, stats) {
    let {shots, injury, kills} = stats;
    let score = shots * 1 + injury * 4 + kills * 4;
    let statel = document.getElementById(`stats${id}`);
    statel.getElementsByClassName('score')[0].childNodes[1].innerText = score;
    statel.getElementsByClassName('shots')[0].childNodes[1].innerText = shots;
    statel.getElementsByClassName('injury')[0].childNodes[1].innerText = injury;
    statel.getElementsByClassName('kills')[0].childNodes[1].innerText = kills;
}

draw_table(0, table1, team0, names1);
draw_table(1, table0, team1, names0);

draw_stats(0, stats1);
draw_stats(1, stats0);

