package coreV3;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.GridBagLayout;
import javax.swing.JLabel;
import java.awt.GridBagConstraints;
import javax.swing.JTextPane;
import java.awt.Insets;
import java.awt.Font;
import java.awt.Color;
import javax.swing.ImageIcon;
import java.awt.Toolkit;

public class AboutPanel extends JDialog {

	private static final long serialVersionUID = 1356333282564255012L;
	private final JPanel contentPanel = new JPanel();

	public AboutPanel() {
		setIconImage(Toolkit.getDefaultToolkit().getImage(AboutPanel.class.getResource("/coreV3/2048.jpg")));
		setTitle("About 2048");
		setType(Type.POPUP);
		setModalityType(ModalityType.TOOLKIT_MODAL);
		setAlwaysOnTop(true);
		setSize(450, 300);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(Color.WHITE);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		GridBagLayout gbl_contentPanel = new GridBagLayout();
		gbl_contentPanel.columnWidths = new int[]{30, 0, 0, 0};
		gbl_contentPanel.rowHeights = new int[]{30, 0, 0};
		gbl_contentPanel.columnWeights = new double[]{0.0, 0.0, 1.0, Double.MIN_VALUE};
		gbl_contentPanel.rowWeights = new double[]{0.0, 1.0, Double.MIN_VALUE};
		contentPanel.setLayout(gbl_contentPanel);
		
		JLabel aboutImage = new JLabel("");
		aboutImage.setIcon(new ImageIcon(AboutPanel.class.getResource("/coreV3/2048.jpg")));
		GridBagConstraints gbc_aboutImage = new GridBagConstraints();
		gbc_aboutImage.insets = new Insets(0, 0, 0, 5);
		gbc_aboutImage.gridx = 1;
		gbc_aboutImage.gridy = 1;
		contentPanel.add(aboutImage, gbc_aboutImage);
		
		JTextPane aboutTXT = new JTextPane();
		aboutTXT.setFont(new Font("Dialog", Font.PLAIN, 14));
		aboutTXT.setEditable(false);
		aboutTXT.setText("Product Name:2048\r\nVersion:1.0.0\r\n\r\nMade by Sean Cheng\r\nUI Designed by Sean Cheng\r\n\r\nEmail:seancheng33@gmail.com\r\n");
		GridBagConstraints gbc_aboutTXT = new GridBagConstraints();
		gbc_aboutTXT.fill = GridBagConstraints.BOTH;
		gbc_aboutTXT.gridx = 2;
		gbc_aboutTXT.gridy = 1;
		contentPanel.add(aboutTXT, gbc_aboutTXT);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			
				JButton okButton = new JButton("OK");
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						dispose();
					}
				});
				//okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				//getRootPane().setDefaultButton(okButton);
			
//			{
//				JButton cancelButton = new JButton("Cancel");
//				cancelButton.setActionCommand("Cancel");
//				buttonPane.add(cancelButton);
//			}
		}
	}

}
