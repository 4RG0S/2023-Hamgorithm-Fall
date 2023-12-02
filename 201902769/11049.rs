use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed");
    let n = buffer.trim().parse::<usize>().unwrap();

    let mut arr = vec![vec![0; 2]; n];
    for i in 0..n {
        buffer.clear();
        io::stdin().read_line(&mut buffer).expect("Failed");

        let mut iter = buffer.split_whitespace();
        let a = iter.next().unwrap().parse::<i32>().unwrap();
        let b = iter.next().unwrap().parse::<i32>().unwrap();
        
        arr[i][0] = a;
        arr[i][1] = b;
    }

    let mut dp = vec![vec![0; n]; n];

    for term in 1..n {
        for start in 0..n-term {

            dp[start][start + term] = i32::MAX;

            for t in start..(start + term) {
                let cur = dp[start][t] + dp[t + 1][start + term] + arr[start][0] * arr[t][1] * arr[start + term][1];
                dp[start][start + term] = std::cmp::min(dp[start][start + term], cur);
            }
        }
    }

    print!("{}", dp[0][n - 1]);
}
