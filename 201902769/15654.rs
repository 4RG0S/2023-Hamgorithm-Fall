use std::fmt::Write;
use std::io::{self, Read};

fn combination(arr: &Vec<i32>, v: &mut Vec<i32>, m: usize, visited: &mut Vec<bool>, output: &mut String) {
    if v.len() == m {
        let line: Vec<String> = v.iter().map(|&i| i.to_string()).collect();
        writeln!(output, "{}", line.join(" ")).ok();
        return;
    }

    for i in 0..arr.len() {
        if visited[i] {
            continue;
        }
        visited[i] = true;
        v.push(arr[i]);
        combination(arr, v, m, visited, output);
        visited[i] = false;
        v.pop();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let a: usize = iter.next().unwrap().parse().unwrap();
    let b: usize = iter.next().unwrap().parse().unwrap();

    let arr: Vec<i32> = (0..a).map(|_| iter.next().unwrap().parse().unwrap()).collect();

    let mut sorted_arr = arr.clone();
    sorted_arr.sort();

    let mut v: Vec<i32> = Vec::new();
    let mut visited = vec![false; a];
    let mut output = String::new();

    combination(&sorted_arr, &mut v, b, &mut visited, &mut output);

    print!("{}", output);
}
