package coreV2;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main extends JFrame {

	/**
	 * 第二个版本，改善了移动的算法，
	 * 完成了所有的判断算法
	 * 添加了失败和胜利的对话框
	 * 优化数字的颜色
	 */
	private static final long serialVersionUID = 7508246293443478394L;
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main frame = new Main();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Main() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//setBounds(100, 100, 600, 600);
		setSize(600,600);
		setTitle("2048");
		setResizable(false);
		setLocationRelativeTo(null);
		contentPane = new GamePanel();
		setContentPane(contentPane);
		pack();
	}
}
