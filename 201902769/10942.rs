use std::io::{self, BufRead, Write};

fn fill_palindrome_table(v: Vec<i32>) -> Vec<Vec<i32>> {
    let n = v.len();
    let mut dp = vec![vec![0; n]; n];

    for i in 0..n {
        dp[i][i] = 1;
    }

    for i in 0..n-1 {
        if v[i] == v[i+1] {
            dp[i][i+1] = 1;
        }
    }

    for len in 2..=n {
        for start in 0..=n-len {
            let end = start + len - 1;
            if v[start] == v[end] && dp[start+1][end-1] == 1 {
                dp[start][end] = 1;
            }
        }
    }

    dp
}

fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let input = stdin.lock();
    let mut output = io::BufWriter::new(stdout.lock());
    let mut lines = input.lines();

    let n: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();

    let v: Vec<i32> = lines.next().unwrap().unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let m: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let dp: Vec<Vec<i32>> = fill_palindrome_table(v);

    for line in lines.take(m as usize) {
        let numbers: Vec<i32> = line.unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();

        let a = numbers[0];
        let b = numbers[1];

        if dp[a as usize - 1][b as usize - 1] == 1 {
            writeln!(output, "1").unwrap();
        } else {
            writeln!(output, "0").unwrap();
        }
    }
}
