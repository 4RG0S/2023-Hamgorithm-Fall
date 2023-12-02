use std::io;

struct Line {
    a: (i128, i128),
    b: (i128, i128),
}

impl Line {
    fn new(a: (i128, i128), b: (i128, i128)) -> Self {
        Self { a, b }
    }

    fn ccw(&self, c: (i128, i128)) -> i128 {
        let (ax, ay) = self.a;
        let (bx, by) = self.b;
        let (cx, cy) = c;
        (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    }

    fn within(&self, c: (i128, i128)) -> bool {
        let (ax, ay) = self.a;
        let (bx, by) = self.b;
        let (cx, cy) = c;
        let min_x = ax.min(bx);
        let max_x = ax.max(bx);
        let min_y = ay.min(by);
        let max_y = ay.max(by);
        cx >= min_x && cx <= max_x && cy >= min_y && cy <= max_y
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.trim().split_whitespace();
    let line1 = Line::new(
        (iter.next().unwrap().parse().unwrap(), iter.next().unwrap().parse().unwrap()),
        (iter.next().unwrap().parse().unwrap(), iter.next().unwrap().parse().unwrap()),
    );

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.trim().split_whitespace();
    let line2 = Line::new(
        (iter.next().unwrap().parse().unwrap(), iter.next().unwrap().parse().unwrap()),
        (iter.next().unwrap().parse().unwrap(), iter.next().unwrap().parse().unwrap()),
    );

    let ccw1 = line1.ccw(line2.a) * line1.ccw(line2.b);
    let ccw2 = line2.ccw(line1.a) * line2.ccw(line1.b);

    // ccw1, ccw2 둘 다 0인 경우는 두 선분이 일직선 상에 있는 경우
    if ccw1 == 0 && ccw2 == 0 {
        // 두 선분이 일직선 상에 있는 경우, 두 선분이 겹치는지 확인
        // 4개 다 비교하는 이유는 포함 관계인 경우도 있기 때문
        if line1.within(line2.a) || line1.within(line2.b) || line2.within(line1.a) || line2.within(line1.b){
            println!("{}", 1);
        } else {
            println!("{}", 0);
        }
    }
    else if ccw1 <= 0 && ccw2 <= 0 {
        println!("{}", 1);
    } else {
        println!("{}", 0);
    }
}
