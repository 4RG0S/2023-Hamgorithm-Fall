use std::io;
struct Vector {
    x: f64,
    y: f64,
}

fn add_vector(a: Vector, b: Vector, c: Vector) -> f64 {
    let result = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    result as f64 / 2.0
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    let n = buf.trim().parse::<usize>().unwrap();
    let mut arr = vec![vec![2.0; 2]; n];
    for i in 0..n {
        let mut buf = String::new();
        io::stdin().read_line(&mut buf).unwrap();
        let mut iter = buf.trim().split_whitespace();
        arr[i][0] = iter.next().unwrap().parse::<f64>().unwrap();
        arr[i][1] = iter.next().unwrap().parse::<f64>().unwrap();
    }

    let mut result = 0.0;
    for i in 2..n {
        let a = Vector { x: arr[0][0], y: arr[0][1] };
        let b = Vector { x: arr[i - 1][0], y: arr[i - 1][1] };
        let c = Vector { x: arr[i][0], y: arr[i][1] };
        result += add_vector(a, b, c);
    }
    println!("{:.1}", result.abs());
}
