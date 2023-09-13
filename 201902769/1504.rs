use std::io;

fn shortest_path(start:i32, end:i32, edges:&[Vec<(i32, i32)>; 801]) -> i32 {
    let mut costs = vec![i32::max_value(); edges.len()];
    costs[start as usize] = 0;

    let mut queue = Vec::new();
    queue.push(start);

    while !queue.is_empty() {
        let node = queue.pop().unwrap();
        for edge in edges[node as usize].iter() {
            let cost = costs[node as usize] + edge.1;
            if cost < costs[edge.0 as usize] {
                costs[edge.0 as usize] = cost;
                queue.push(edge.0);
            }
        }
    }
    costs[end as usize]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
    let n = iter.next().unwrap();
    let e = iter.next().unwrap();

    let temp: Vec<Vec<(i32, i32)>> = vec![Vec::new(); 801];
    let mut edges: [Vec<(i32, i32)>; 801] = temp.try_into().unwrap_or_else(|v: Vec<Vec<(i32, i32)>>| {
        panic!("Expected a Vec of length {} but it was {}", 801, v.len())
    });
    for _ in 0..e {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        let (a, b, c) = (iter.next().unwrap(), iter.next().unwrap(), iter.next().unwrap());
        edges[a as usize].push((b, c));
        edges[b as usize].push((a, c));
    }
    
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
    let start = iter.next().unwrap();
    let end = iter.next().unwrap();
    let path1 = shortest_path(1, start, &edges);
    let path2 = shortest_path(start, end, &edges);
    let path3 = shortest_path(end, n, &edges);

    let mut result1 = path1
        .checked_add(path2)
        .and_then(|sum| sum.checked_add(path3))
        .unwrap_or(i32::max_value());

    let path1 = shortest_path(1, end, &edges);
    let path2 = shortest_path(end, start, &edges);
    let path3 = shortest_path(start, n, &edges);

    let mut result2 = path1
        .checked_add(path2)
        .and_then(|sum| sum.checked_add(path3))
        .unwrap_or(i32::max_value());
    
    if result1 == i32::max_value() && result2 == i32::max_value() {
        print!("{}", -1);
    }
    else {
        if result1 < result2 {
            print!("{}", result1);
        }
        else {
            print!("{}", result2);
        }
    }
}