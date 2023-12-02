use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let nm: Vec<usize> = lines.next().unwrap().unwrap().split_whitespace()
                              .map(|x| x.parse().unwrap()).collect();

    let numbers: Vec<i32> = lines.next().unwrap().unwrap().split_whitespace()
                                .map(|x| x.parse::<i32>().unwrap()).collect();

    // 누적합 계산
    let mut prefix_sum = vec![0i32; numbers.len() + 1];
    for i in 0..numbers.len() {
        prefix_sum[i + 1] = prefix_sum[i] + numbers[i];
    }

    let stdout = io::stdout();
    let mut handle = io::BufWriter::new(stdout.lock());

    for _ in 0..nm[1] {
        let range: Vec<usize> = lines.next().unwrap().unwrap().split_whitespace()
                                    .map(|x| x.parse().unwrap()).collect();

        let sum: i32 = prefix_sum[range[1]] - prefix_sum[range[0] - 1];
        writeln!(handle, "{}", sum).unwrap();
    }
}
