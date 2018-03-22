package core;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements KeyListener {

	private static final long serialVersionUID = 2545803526458461245L;

	private boolean flag = true;

	private int[][] map = { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 },
			{ 0, 0, 0, 0 } };

	/**
	 * Create the panel.
	 * 
	 */
	public GamePanel() {
		setPreferredSize(new Dimension(600, 600));
		setFocusable(true);
		addKeyListener(this);
	}

	@Override
	public void paint(Graphics g) {
		super.paint(g);
		drawMap(g);

	}

	private void startGame(Graphics g) {
		int startNum = 0;
		while (startNum < 2) {
			int x = (int) (Math.random() * 4);
			int y = (int) (Math.random() * 4);
			if (map[x][y] == 0) {
				map[x][y] = 2;
			}
			startNum++;
		}
	}

	private void drawMap(Graphics g) {
		if (flag) {
			startGame(g);
			flag = false;
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				g.setColor(Color.BLACK);
				g.drawRect(i * 150, j * 150, 150, 150);
				if (map[i][j] != 0) {
					int num = map[i][j];
					switch (num) {
					case 2:
						g.setColor(Color.LIGHT_GRAY);
						break;
					case 4:
						g.setColor(Color.GRAY);
						break;
					case 8:
						g.setColor(Color.DARK_GRAY);
						break;
					case 16:
						g.setColor(Color.RED);
						break;
					case 32:
						g.setColor(Color.PINK);
						break;
					case 64:
						g.setColor(Color.ORANGE);
						break;
					case 128:
						g.setColor(Color.YELLOW);
						break;
					case 256:
						g.setColor(Color.GREEN);
						break;
					case 512:
						g.setColor(Color.MAGENTA);
						break;
					case 1024:
						g.setColor(Color.CYAN);
						break;
					case 2048:
						g.setColor(Color.BLUE);
						break;
					}
					g.fill3DRect(i * 150 + 5, j * 150 + 5, 140, 140, true);
					g.setColor(Color.BLACK);
					g.setFont(new Font("", Font.BOLD, 32));
					g.drawString(Integer.toString(num), i * 150 + 65,
							j * 150 + 85);
				}
			}
		}
	}

	// 进行判断，将数字移动或者合并
	private void moveLeft() {
		/*
		 * 这个是第一版，最原始的关于想左移动的思路和做法， 想判断第一和第二格是可以移动还是可以合并，如果这两个条件都不符合就什么都不做
		 * 然后再判断第二和第三的关系，第二和第一的关系判断完成在进行第一和第二的判断 然后是判断第三和第四，再第二和第三，再第二和第一
		 */

		// for (int i = 0; i < 4; i++) {
		//
		// if (map[0][i] == 0 && map[1][i] != 0) {
		// map[0][i] = map[1][i];
		// map[1][i] = 0;
		// } else {
		// if (map[0][i] == map[1][i]) {
		// map[0][i] = map[1][i] + map[0][i];
		// map[1][i] = 0;
		// }
		// }
		//
		//
		// if (map[1][i] == 0 && map[2][i] != 0) {
		// map[1][i] = map[2][i];
		// map[2][i] = 0;
		// if (map[0][i] == 0 && map[1][i] != 0) {
		// map[0][i] = map[1][i];
		// map[1][i] = 0;
		// } else {
		// if (map[0][i] == map[1][i]) {
		// map[0][i] = map[1][i] + map[0][i];
		// map[1][i] = 0;
		// }
		// }
		// }else{
		// if(map[1][i]==map[2][i]){
		// map[1][i] = map[2][i]+map[1][i];
		// map[2][i] = 0;
		// }
		// }
		//
		//
		// if (map[2][i] == 0 && map[3][i] != 0) {
		// map[2][i] = map[3][i];
		// map[3][i] = 0;
		// if (map[1][i] == 0 && map[2][i] != 0) {
		// map[1][i] = map[2][i];
		// map[2][i] = 0;
		// if (map[0][i] == 0 && map[1][i] != 0) {
		// map[0][i] = map[1][i];
		// map[1][i] = 0;
		// } else {
		// if (map[0][i] == map[1][i]) {
		// map[0][i] = map[1][i] + map[0][i];
		// map[1][i] = 0;
		// }
		// }
		// }else{
		// if(map[1][i]==map[2][i]){
		// map[1][i] = map[2][i]+map[1][i];
		// map[2][i] = 0;
		// }
		// }
		// }else{
		// if(map[2][i]==map[3][i]){
		// map[2][i] = map[3][i]+map[2][i];
		// map[3][i] = 0;
		// }
		// }
		// }

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 3; j++) {
				int k = j;
				while (k > -1) {
					if (map[k][i] == 0 && map[k + 1][i] != 0) {
						map[k][i] = map[k + 1][i];
						map[k + 1][i] = 0;
					} else {
						if (map[k][i] == map[k + 1][i]) {
							map[k][i] = map[k + 1][i] + map[k][i];
							map[k + 1][i] = 0;
							break;
						}

					}
					k--;
				}
			}
		}
		addNewNum();
	}

	private void moveRight() {
		// for (int i = 4; i > 0; i--) {
		// //
		// if (map[3][i - 1] == 0 && map[2][i - 1] != 0) {
		// map[3][i - 1] = map[2][i - 1];
		// map[2][i - 1] = 0;
		// } else {
		// if (map[3][i - 1] == map[2][i - 1]) {
		// map[3][i - 1] = map[2][i - 1] + map[3][i - 1];
		// map[2][i - 1] = 0;
		// }
		// }
		//
		// //
		// if (map[2][i - 1] == 0 && map[1][i - 1] != 0) {
		// map[2][i - 1] = map[1][i - 1];
		// map[1][i - 1] = 0;
		// if (map[3][i - 1] == 0 && map[2][i - 1] != 0) {
		// map[3][i - 1] = map[2][i - 1];
		// map[2][i - 1] = 0;
		// } else {
		// if (map[3][i - 1] == map[2][i - 1]) {
		// map[3][i - 1] = map[2][i - 1] + map[3][i - 1];
		// map[2][i - 1] = 0;
		// }
		// }
		// } else {
		// if (map[2][i - 1] == map[1][i - 1]) {
		// map[2][i - 1] = map[1][i - 1] + map[2][i - 1];
		// map[1][i - 1] = 0;
		// }
		// }
		//
		// //
		// if (map[1][i - 1] == 0 && map[0][i - 1] != 0) {
		// map[1][i - 1] = map[0][i - 1];
		// map[0][i - 1] = 0;
		// if (map[2][i - 1] == 0 && map[1][i - 1] != 0) {
		// map[2][i - 1] = map[1][i - 1];
		// map[1][i - 1] = 0;
		// if (map[3][i - 1] == 0 && map[2][i - 1] != 0) {
		// map[3][i - 1] = map[2][i - 1];
		// map[2][i - 1] = 0;
		// } else {
		// if (map[3][i - 1] == map[2][i - 1]) {
		// map[3][i - 1] = map[2][i - 1] + map[0][i - 1];
		// map[2][i - 1] = 0;
		// }
		// }
		// } else {
		// if (map[2][i - 1] == map[1][i - 1]) {
		// map[2][i - 1] = map[1][i - 1] + map[2][i - 1];
		// map[1][i - 1] = 0;
		// }
		// }
		// } else {
		// if (map[1][i - 1] == map[0][i - 1]) {
		// map[1][i - 1] = map[0][i - 1] + map[1][i - 1];
		// map[0][i - 1] = 0;
		// }
		// }
		// }
		for (int i = 4; i > 0; i--) {
			for (int j = 0; j < 3; j++) {
				int k = j;
				while (k > -1) {
					if (map[3 - k][i - 1] == 0 && map[2 - k][i - 1] != 0) {
						map[3 - k][i - 1] = map[2 - k][i - 1];
						map[2 - k][i - 1] = 0;
					} else {
						if (map[3 - k][i - 1] == map[2 - k][i - 1]) {
							map[3 - k][i - 1] = map[2 - k][i - 1]
									+ map[3 - k][i - 1];
							map[2 - k][i - 1] = 0;
							break;
						}
					}
					k--;
				}
			}
		}
		addNewNum();
	}

	private void moveDown() {
		// for (int i = 0; i < 4; i++) {
		// //
		// if (map[i][3] == 0 && map[i][2] != 0) {
		// map[i][3] = map[i][2];
		// map[i][2] = 0;
		// } else {
		// if (map[i][3] == map[i][2]) {
		// map[i][3] = map[i][2] + map[i][3];
		// map[i][2] = 0;
		// }
		// }
		//
		// //
		// if (map[i][2] == 0 && map[i][1] != 0) {
		// map[i][2] = map[i][1];
		// map[i][1] = 0;
		// if (map[i][3] == 0 && map[i][2] != 0) {
		// map[i][3] = map[i][2];
		// map[i][2] = 0;
		// } else {
		// if (map[i][3] == map[i][2]) {
		// map[i][3] = map[i][2] + map[i][3];
		// map[i][2] = 0;
		// }
		// }
		// } else {
		// if (map[i][2] == map[i][1]) {
		// map[i][2] = map[i][1] + map[i][2];
		// map[i][1] = 0;
		// }
		// }
		//
		// //
		// if (map[i][1] == 0 && map[i][0] != 0) {
		// map[i][1] = map[i][0];
		// map[i][0] = 0;
		// if (map[i][2] == 0 && map[i][1] != 0) {
		// map[i][2] = map[i][1];
		// map[i][1] = 0;
		// if (map[i][3] == 0 && map[i][2] != 0) {
		// map[i][3] = map[i][2];
		// map[i][2] = 0;
		// } else {
		// if (map[i][3] == map[i][2]) {
		// map[i][3] = map[i][2] + map[i][3];
		// map[i][2] = 0;
		// }
		// }
		// } else {
		// if (map[i][2] == map[i][1]) {
		// map[i][2] = map[i][1] + map[i][2];
		// map[i][1] = 0;
		// }
		// }
		// } else {
		// if (map[i][1] == map[i][0]) {
		// map[i][1] = map[i][0] + map[i][1];
		// map[i][0] = 0;
		// }
		// }
		// }

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 3; j++) {
				int k = j;
				while (k > -1) {
					if (map[i][3 - k] == 0 && map[i][2 - k] != 0) {
						map[i][3 - k] = map[i][2 - k];
						map[i][2 - k] = 0;
					} else {
						if (map[i][3 - k] == map[i][2 - k]) {
							map[i][3 - k] = map[i][2 - k] + map[i][3 - k];
							map[i][2 - k] = 0;
							break;
						}
					}
					k--;
				}
			}
		}
		addNewNum();
	}

	private void moveUp() {
		// for (int i = 4; i > 0; i--) {
		// //
		// if (map[i - 1][0] == 0 && map[i - 1][1] != 0) {
		// map[i - 1][0] = map[i - 1][1];
		// map[i - 1][1] = 0;
		// } else {
		// if (map[i - 1][0] == map[i - 1][1]) {
		// map[i - 1][0] = map[i - 1][1] + map[i - 1][0];
		// map[i - 1][1] = 0;
		// }
		// }
		//
		// //
		// if (map[i - 1][1] == 0 && map[i - 1][2] != 0) {
		// map[i - 1][1] = map[i - 1][2];
		// map[i - 1][2] = 0;
		// if (map[i - 1][0] == 0 && map[i - 1][1] != 0) {
		// map[i - 1][0] = map[i - 1][1];
		// map[i - 1][1] = 0;
		// } else {
		// if (map[i - 1][0] == map[i - 1][1]) {
		// map[i - 1][0] = map[i - 1][1] + map[i - 1][0];
		// map[i - 1][1] = 0;
		// }
		// }
		// } else {
		// if (map[i - 1][1] == map[i - 1][2]) {
		// map[i - 1][1] = map[i - 1][2] + map[i - 1][1];
		// map[i - 1][2] = 0;
		// }
		// }
		//
		// //
		// if (map[i - 1][2] == 0 && map[i - 1][3] != 0) {
		// map[i - 1][2] = map[i - 1][3];
		// map[i - 1][3] = 0;
		// if (map[i - 1][1] == 0 && map[i - 1][2] != 0) {
		// map[i - 1][1] = map[i - 1][2];
		// map[i - 1][2] = 0;
		// if (map[i - 1][0] == 0 && map[i - 1][1] != 0) {
		// map[i - 1][0] = map[i - 1][1];
		// map[i - 1][1] = 0;
		// } else {
		// if (map[i - 1][0] == map[i - 1][1]) {
		// map[i - 1][0] = map[i - 1][1] + map[i - 1][0];
		// map[i - 1][1] = 0;
		// }
		// }
		// } else {
		// if (map[i - 1][1] == map[i - 1][2]) {
		// map[i - 1][1] = map[i - 1][2] + map[i - 1][1];
		// map[i - 1][2] = 0;
		// }
		// }
		// } else {
		// if (map[i - 1][2] == map[i - 1][3]) {
		// map[i - 1][2] = map[i - 1][3] + map[i - 1][2];
		// map[i - 1][3] = 0;
		// }
		// }
		// }

		for (int i = 4; i > 0; i--) {
			for (int j = 0; j < 3; j++) {
				int k = j;
				while (k > -1) {
					if (map[i - 1][k] == 0 && map[i - 1][k + 1] != 0) {
						map[i - 1][k] = map[i - 1][k + 1];
						map[i - 1][k + 1] = 0;
					} else {
						if (map[i - 1][k] == map[i - 1][k + 1]) {
							map[i - 1][k] = map[i - 1][k + 1] + map[i - 1][k];
							map[i - 1][k + 1] = 0;
							break;
						}
					}
					k--;
				}
			}
		}

		addNewNum();
	}

	// 添加新的数字出现
	private void addNewNum() {
		boolean add = true;
		while (add) {
			int x = (int) (Math.random() * 4);
			int y = (int) (Math.random() * 4);
			if (map[x][y] == 0) {
				map[x][y] = 2;
				add = false;
				break;
			}
		}
	}

	private boolean isWin(int[][] map) {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (map[i][j] == 2048) {
					return true;
				}
			}
		}
		return false;
	}

	// 判断是不是数字全部填满,只要填满了就不可以移动
	// 还没有添加判断满了之后是不是还可以移动
	private boolean isFail(int[][] map) {
		int k = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (map[i][j] != 0) {
					k++;
				}
			}
		}
		if (k == 16) {
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (i + 1 < 4 && i - 1 > 0 && j - 1 > 0 && j + 1 < 4) {
						if (map[i][j] == map[i][j + 1]
								|| map[i][j] == map[i + 1][j]
								|| map[i][j] == map[i - 1][j]
								|| map[i][j] == map[i][j - 1]) {
							return true;
						}
					} else {
						return false;
					}
				}
			}
		}
		return true;
	}

	@Override
	public void keyPressed(KeyEvent arg0) {
		if (arg0.getKeyCode() == KeyEvent.VK_LEFT) {
			if (isFail(map)) {
				moveLeft();
				repaint();
			}
			if (isWin(map)) {
				System.out.println("胜出");
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_RIGHT) {
			if (isFail(map)) {
				moveRight();
				repaint();
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_UP) {
			if (isFail(map)) {
				moveUp();
				repaint();
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_DOWN) {
			if (isFail(map)) {
				moveDown();
				repaint();
			}
		}
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
	}

	@Override
	public void keyTyped(KeyEvent arg0) {
	}

}
