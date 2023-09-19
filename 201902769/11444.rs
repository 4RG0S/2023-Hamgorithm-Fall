use std::io;

fn mul_arr(arr1: [[i64; 2]; 2], arr2: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    let mut res = [[0; 2]; 2];

    for i in 0..2 {
        for j in 0..2 {
            for z in 0..2 {
                res[i][j] += (arr1[i][z] * arr2[z][j]) % 1000000007;
                res[i][j] %= 1000000007;
            }
        }
    }
    res
}

fn pow_arr(arr: [[i64; 2]; 2], n: i64) -> [[i64; 2]; 2] {
    if n == 1 {
        return arr;
    }

    let mut res = pow_arr(arr, n / 2);
    res = mul_arr(res, res);

    if n % 2 == 1 {
        res = mul_arr(res, arr);
    }

    res
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed");
    let n = buffer.trim().parse::<i64>().unwrap();
    
    let arr: [[i64; 2]; 2] = [[1, 1], [1, 0]];
    if n == 0 {
        println!("{}", 0);
        return;
    }
    else {
        let res = pow_arr(arr, n);
        println!("{}", res[0][1]);
    }
}