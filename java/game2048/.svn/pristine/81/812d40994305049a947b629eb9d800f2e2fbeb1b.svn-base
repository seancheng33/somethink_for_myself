package coreV3;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class StatusPanel extends JPanel {

	private static final long serialVersionUID = -2264873746280434874L;

	public StatusPanel() {
		setPreferredSize(new Dimension(250,600));
		setBackground(new Color(68,153,238));
		GridBagLayout gridBagLayout = new GridBagLayout();
		gridBagLayout.columnWidths = new int[]{230, 0};
		gridBagLayout.rowHeights = new int[]{50, 0, 31, 30, 31, 31, 31, 30, 34, 34, 34, 0};
		gridBagLayout.columnWeights = new double[]{1.0, Double.MIN_VALUE};
		gridBagLayout.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
		setLayout(gridBagLayout);
		
		JLabel playImage = new JLabel("");
		playImage.setIcon(new ImageIcon(StatusPanel.class.getResource("/coreV3/control.png")));
		GridBagConstraints gbc_playImage = new GridBagConstraints();
		gbc_playImage.anchor = GridBagConstraints.NORTH;
		gbc_playImage.insets = new Insets(0, 0, 5, 0);
		gbc_playImage.gridx = 0;
		gbc_playImage.gridy = 1;
		add(playImage, gbc_playImage);
		
		JLabel lblToMoveAll = new JLabel("to move all tiles.");
		lblToMoveAll.setFont(new Font("", Font.PLAIN, 22));
		GridBagConstraints gbc_lblToMoveAll = new GridBagConstraints();
		gbc_lblToMoveAll.anchor = GridBagConstraints.NORTH;
		gbc_lblToMoveAll.insets = new Insets(0, 0, 5, 0);
		gbc_lblToMoveAll.gridx = 0;
		gbc_lblToMoveAll.gridy = 2;
		add(lblToMoveAll, gbc_lblToMoveAll);
		
		JLabel label_2 = new JLabel("When two tiles with");
		label_2.setFont(new Font("", Font.PLAIN, 22));
		GridBagConstraints gbc_label_2 = new GridBagConstraints();
		gbc_label_2.anchor = GridBagConstraints.NORTH;
		gbc_label_2.insets = new Insets(0, 0, 5, 0);
		gbc_label_2.gridx = 0;
		gbc_label_2.gridy = 4;
		add(label_2, gbc_label_2);
		
		JLabel label_3 = new JLabel("the same number touch.");
		label_3.setFont(new Font("", Font.PLAIN, 22));
		GridBagConstraints gbc_label_3 = new GridBagConstraints();
		gbc_label_3.anchor = GridBagConstraints.NORTH;
		gbc_label_3.insets = new Insets(0, 0, 5, 0);
		gbc_label_3.gridx = 0;
		gbc_label_3.gridy = 5;
		add(label_3, gbc_label_3);
		
		JLabel label_4 = new JLabel("They merge into one!");
		label_4.setFont(new Font("", Font.PLAIN, 22));
		GridBagConstraints gbc_label_4 = new GridBagConstraints();
		gbc_label_4.anchor = GridBagConstraints.NORTH;
		gbc_label_4.insets = new Insets(0, 0, 5, 0);
		gbc_label_4.gridx = 0;
		gbc_label_4.gridy = 6;
		add(label_4, gbc_label_4);
		
			JLabel label_5 = new JLabel("Join the number");
			label_5.setFont(new Font("", Font.PLAIN, 24));
			GridBagConstraints gbc_label_5 = new GridBagConstraints();
			gbc_label_5.anchor = GridBagConstraints.NORTH;
			gbc_label_5.insets = new Insets(0, 0, 5, 0);
			gbc_label_5.gridx = 0;
			gbc_label_5.gridy = 8;
			add(label_5, gbc_label_5);
		
		JLabel lblAnd = new JLabel("and");
		lblAnd.setFont(new Font("", Font.PLAIN, 24));
		GridBagConstraints gbc_lblAnd = new GridBagConstraints();
		gbc_lblAnd.anchor = GridBagConstraints.NORTH;
		gbc_lblAnd.insets = new Insets(0, 0, 5, 0);
		gbc_lblAnd.gridx = 0;
		gbc_lblAnd.gridy = 9;
		add(lblAnd, gbc_lblAnd);
		
		JLabel label_7 = new JLabel("get the 2048 tile!");
		label_7.setFont(new Font("", Font.PLAIN, 24));
		GridBagConstraints gbc_label_7 = new GridBagConstraints();
		gbc_label_7.anchor = GridBagConstraints.NORTH;
		gbc_label_7.gridx = 0;
		gbc_label_7.gridy = 10;
		add(label_7, gbc_label_7);
		
	}
}
