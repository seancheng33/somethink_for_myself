package coreV3;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Menu;
import java.awt.MenuBar;
import java.awt.MenuItem;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Toolkit;

public class Main extends JFrame {

	/**
	 * 第三个版本
	 * 在第二个版本已经完成所有的算法的基础上
	 * 这个版本主要的任务是在于界面的完善
	 * 
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
		setIconImage(Toolkit.getDefaultToolkit().getImage(Main.class.getResource("/coreV3/2048.jpg")));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//setBounds(100, 100, 600, 600);
		setSize(850,600);
		setTitle("Game 2048 Develement with Java");
		setResizable(false);
		setLocationRelativeTo(null);
		
		MenuBar menuBar = new MenuBar();
		//游戏菜单，包括重新开始新游戏和退出
		Menu gameMenu = new Menu("Game");
		MenuItem  newMenu = new MenuItem("New Game");
		newMenu.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				GamePanel.resetMap();
				GamePanel.startGame();
				repaint();
			}
		});
		MenuItem  exitMenu = new MenuItem("Exit");
		exitMenu.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				System.exit(0);
			}
		});
		gameMenu.add(newMenu);
		gameMenu.add(exitMenu);
		
		//帮助菜单，包括游戏的规则、游戏技巧和关于游戏，版本介绍
		Menu helpMenu = new Menu("Help");
		//MenuItem  howToPlayMenu = new MenuItem("How to play?");
		MenuItem  aboutMenu = new MenuItem("About 2048...");
		
		//helpMenu.add(howToPlayMenu);
		helpMenu.add(aboutMenu);
		helpMenu.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				AboutPanel dialog = new AboutPanel();
				//dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				dialog.setVisible(true);
			}
		});
		
		menuBar.add(gameMenu);
		menuBar.add(helpMenu);
		setMenuBar(menuBar);
	
		contentPane = new JPanel();
		setContentPane(contentPane);
		
		JPanel gamePane = new GamePanel();
		JPanel statusPane = new StatusPanel();
		
		contentPane.setLayout(new BorderLayout());
		contentPane.add(gamePane,BorderLayout.CENTER);
		contentPane.add(statusPane,BorderLayout.EAST);
		pack();
	}
}
