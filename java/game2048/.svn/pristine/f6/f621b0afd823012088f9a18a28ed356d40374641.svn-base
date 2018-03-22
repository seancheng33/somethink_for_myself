package coreV3;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class GamePanel extends JPanel implements KeyListener {

	private static final long serialVersionUID = 2545803526458461245L;

	private boolean flag = true;

	private static int[][] map = { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 },
			{ 0, 0, 0, 0 } };

	private final int LEFT = 0;
	private final int RIGHT = 1;
	private final int UP = 2;
	private final int DOWN = 3;

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

	public static void startGame() {
		int startNum = 0;
		while (startNum < 2) {
			int x = (int) (Math.random() * 4);
			int y = (int) (Math.random() * 4);
			if (map[x][y] == 0) {
				map[x][y] = 2;
				startNum++;
			}
		}
	}

	public static void resetMap() {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				map[i][j] = 0;
			}
		}
	}

	private void drawMap(Graphics g) {
		if (flag) {
			startGame();
			flag = false;
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				g.setColor(Color.BLACK);
				g.drawRect(i * 150, j * 150, 150, 150);

				if (map[i][j] != 0) {
					int num = map[i][j];

					// 不同的数字，用不同的底色
					switch (num) {
					case 2:
						g.setColor(new Color(255, 255, 102));
						break;
					case 4:
						g.setColor(new Color(255, 255, 00));
						break;
					case 8:
						g.setColor(new Color(255, 204, 152));
						break;
					case 16:
						g.setColor(new Color(255, 204, 00));
						break;
					case 32:
						g.setColor(new Color(255, 152, 204));
						break;
					case 64:
						g.setColor(new Color(255, 152, 152));
						break;
					case 128:
						g.setColor(new Color(255, 152, 102));
						break;
					case 256:
						g.setColor(new Color(255, 152, 00));
						break;
					case 512:
						g.setColor(new Color(255, 102, 102));
						break;
					case 1024:
						g.setColor(new Color(255, 102, 00));
						break;
					case 2048:
						g.setColor(new Color(255, 00, 51));
						break;
					}
					g.fill3DRect(i * 150 + 5, j * 150 + 5, 140, 140, true);
					g.setColor(Color.BLACK);
					g.setFont(new Font("", Font.BOLD, 32));
					String strNumber = Integer.toString(num);

					// 根据数字的不同，定义出他们不同的X轴，使得数字可以居中
					int numX = 0;
					switch (num) {
					case 2:
						numX = 65;
						break;
					case 4:
						numX = 65;
						break;
					case 8:
						numX = 65;
						break;
					case 16:
						numX = 60;
						break;
					case 32:
						numX = 60;
						break;
					case 64:
						numX = 60;
						break;
					case 128:
						numX = 50;
						break;
					case 256:
						numX = 50;
						break;
					case 512:
						numX = 50;
						break;
					case 1024:
						numX = 40;
						break;
					case 2048:
						numX = 40;
						break;
					}
					g.drawString(strNumber, i * 150 + numX, j * 150 + 85);
				}
			}
		}
	}

	// 进行判断，将数字移动或者合并
	private void moveLeft() {

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

	private boolean isFail(int[][] map) {

		// 查看是不是16格全填满
		int numFull = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (map[i][j] != 0) {
					numFull++;
				}
			}
		}

		// 16格每个都进行和上下左右比较，看是否有相同的，有相同就代表可以移动
		int moveStep = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {

				if ((i - 1) > -1 && map[i][j] == map[i - 1][j]) {
					moveStep++;
				}
				if ((i + 1) < 4 && map[i][j] == map[i + 1][j]) {
					moveStep++;
				}
				if ((j - 1) > -1 && map[i][j] == map[i][j - 1]) {
					moveStep++;
				}
				if ((j + 1) < 4 && map[i][j] == map[i][j + 1]) {
					moveStep++;
				}

			}
		}

		// 如果有16格全满，且没有可以移动的，就表示失败
		if (numFull == 16 && moveStep == 0) {
			return true;
		}
		return false;
	}

	private boolean canMove(int[][] map, int direction) {
		//
		int canMoveNum = 0;
		switch (direction) {
		case LEFT:
			for (int i = 0; i < 4; i++) {
				// 判断有空格的移动
				if (map[3][i] != 0 && map[2][i] == 0) {
					canMoveNum++;
				}
				if (map[2][i] != 0 && map[1][i] == 0) {
					canMoveNum++;
				}
				if (map[1][i] != 0 && map[0][i] == 0) {
					canMoveNum++;
				}
				// 判断是否有可以相加，有相加也算可以移动
				if (map[0][i] != 0 && map[0][i] == map[1][i]) {
					canMoveNum++;
				}
				if (map[1][i] != 0 && map[1][i] == map[2][i]) {
					canMoveNum++;
				}
				if (map[2][i] != 0 && map[2][i] == map[3][i]) {
					canMoveNum++;
				}
			}
			if (canMoveNum > 0) {
				return true;
			}
			break;
		case RIGHT:
			for (int i = 0; i < 4; i++) {
				// 判断有空格的移动
				if (map[2][i] != 0 && map[3][i] == 0) {
					canMoveNum++;
				}
				if (map[1][i] != 0 && map[2][i] == 0) {
					canMoveNum++;
				}
				if (map[0][i] != 0 && map[1][i] == 0) {
					canMoveNum++;
				}
				// 判断是否有可以相加，有相加也算可以移动
				if (map[3][i] != 0 && map[3][i] == map[2][i]) {
					canMoveNum++;
				}
				if (map[2][i] != 0 && map[2][i] == map[1][i]) {
					canMoveNum++;
				}
				if (map[1][i] != 0 && map[1][i] == map[0][i]) {
					canMoveNum++;
				}
			}
			if (canMoveNum > 0) {
				return true;
			}
			break;
		case UP:
			for (int i = 0; i < 4; i++) {
				// 判断有空格的移动
				if (map[i][3] != 0 && map[i][2] == 0) {
					canMoveNum++;
				}
				if (map[i][2] != 0 && map[i][1] == 0) {
					canMoveNum++;
				}
				if (map[i][1] != 0 && map[i][0] == 0) {
					canMoveNum++;
				}
				// 判断是否有可以相加，有相加也算可以移动
				if (map[i][2] != 0 && map[i][3] == map[i][2]) {
					canMoveNum++;
				}
				if (map[i][1] != 0 && map[i][2] == map[i][1]) {
					canMoveNum++;
				}
				if (map[i][0] != 0 && map[i][1] == map[i][0]) {
					canMoveNum++;
				}
			}
			if (canMoveNum > 0) {
				return true;
			}
			break;

		case DOWN:
			for (int i = 0; i < 4; i++) {
				// 判断有空格的移动
				if (map[i][2] != 0 && map[i][3] == 0) {
					canMoveNum++;
				}
				if (map[i][1] != 0 && map[i][2] == 0) {
					canMoveNum++;
				}
				if (map[i][0] != 0 && map[i][1] == 0) {
					canMoveNum++;
				}
				// 判断是否有可以相加，有相加也算可以移动
				if (map[i][3] != 0 && map[i][3] == map[i][2]) {
					canMoveNum++;
				}
				if (map[i][2] != 0 && map[i][2] == map[i][1]) {
					canMoveNum++;
				}
				if (map[i][1] != 0 && map[i][1] == map[i][0]) {
					canMoveNum++;
				}
			}
			if (canMoveNum > 0) {
				return true;
			}
			break;
		}
		return false;
	}

	@Override
	public void keyPressed(KeyEvent arg0) {
		if (arg0.getKeyCode() == KeyEvent.VK_LEFT
				|| arg0.getKeyCode() == KeyEvent.VK_A) {
			if (canMove(map, LEFT)) {
				moveLeft();
				repaint();
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_RIGHT
				|| arg0.getKeyCode() == KeyEvent.VK_D) {
			if (canMove(map, RIGHT)) {
				moveRight();
				repaint();
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_UP
				|| arg0.getKeyCode() == KeyEvent.VK_W) {
			if (canMove(map, UP)) {
				moveUp();
				repaint();
			}
		}
		if (arg0.getKeyCode() == KeyEvent.VK_DOWN
				|| arg0.getKeyCode() == KeyEvent.VK_S) {
			if (canMove(map, DOWN)) {
				moveDown();
				repaint();
			}
		}
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
		// 在移动完成后，按键弹起的时候，判断是否已经胜利，已经胜利则弹出对话框
		if (isWin(map)) {
			int option = JOptionPane.showConfirmDialog(null, "是否重新再玩？",
					"恭喜赢得游戏！", JOptionPane.YES_NO_OPTION);
			if (option == JOptionPane.OK_OPTION) {
				resetMap();
				startGame();
				repaint();
			}
		}

		// 在移动完成后，按键弹起的时候，判断是否还可以移动，如果已经不可以移动，就弹出对话框
		if (isFail(map)) {
			int option = JOptionPane.showConfirmDialog(null, "是否重新再玩？",
					"已经填满，游戏失败！", JOptionPane.YES_NO_OPTION);
			if (option == JOptionPane.OK_OPTION) {
				resetMap();
				startGame();
				repaint();
			}
		}

	}

	@Override
	public void keyTyped(KeyEvent arg0) {
	}

}
