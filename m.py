U
    �^�^]  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZdZe	ed� ze
dd	�Ze�� Zej W nJ   eed
��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX z&e
dd	�Ze
dd	�Ze�� Zej W nJ   eed��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX zd dlZW nF ek
�rp   e	d� e�d� e	d� e�d� d dlZeZY nX dd� Zdd� Zedk�r�e�  dS )�    N�clearz'     >>>>    WON data    <<<<          z(      >>>>    NO  data    <<<<          zG[1;36;40m
___________________________________________________________
au	  [1;36;40m

             **                  **                 M
               **               **                  E 
                ** *********** **                   G
                 ***************                    A
                ******************
              **** @ ****** @ *****
             ***********************                R
            *************************               U
           ***************************              N          
                                        
        ****    ******************     ****         2  
       ******  ********************   ******          
       ******  *********************  ******        0     
       ******  *********************  ******         
       ******  *********************  ******        2     
       ******  *********************  ******          
       ******  *********************  ******        0  
       ******  *********************  ******            
       ******  *********************  ******              
       ******  *********************  ******              
       ******  *********************  ******              
       ******    *****************    ******           
        ****       *************       ****           
                                                    
                ******       *****                 R     
               ********     ********               J      
               ********     ********                     
               ********     ********               S     
               ********     ********               T    
               ********     ********               U      
               ********     ********               D      
               ********     ********               I      
                ******       ******                O      
__________________________________________________________
[1;35;40m      __  __               _      ____        _   _       
[1;33;40m     |  \/  | ___  __ _   / \    |  _ \ _   _| \ | | Hack
[1;32;40m     | |\/| |/ _ \/ _` | / O \   | |_) | | | |  \| |    
[1;30;40m     | |  | |  __/ (_| |/ ___ \  |  _ <| |_| | |\  |    
[1;32;40m     |_|  |_|\___|\__, /_/   \_\ |_| \_\___|||_| \_|    
[1;34;40m                  |___/                                 
[1;35;40m              [Be Cool] mod by RJ studio 2020
[1;32;40m___________________________________________________________
� zfile_auth.txt�rz![1;0;40mPaste Your Auth here :- �wzfile_url.txtzPaste Your URL here :- z,%s Requests isn't installed, installing now.zpip3 install requestsz%s Requests has been installed.c            	      C   s"  t �d� ttd� ttd��} dtdd�}t}d}| |k�rt �d� tt� d}tj	||d�}t
|�}|d	kr|tt� n*|d
kr�tt� ntt� td� tt� |d7 }tdt
|�ddd� td�D ]@}|d d }tdt
t|��d dd� t�d� tj�d� q�q4t �d� t�  d S )Nr   �
z[1;36;40mEnter Amount - zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionr   )Zheadersz<Response [204]>z<Response [200]>zC
[1;31;40m [retry] Check Again your internet connection... [retry]�   z
[1;0;40m
zPlease Wait For Next requestr   )�end�   �d   z[1;36;40m
>>> [+]z% g      �?z[Fzfiglet FINISHED)�os�system�print�name�int�input�	file_auth�	file_url1�requests�get�str�no_data�won_data�bar�range�time�sleep�sys�stdout�write�again)	�s�headZurlZss�size�resZresp�iZpr� r%   �/storage/emulated/0/mega.py�mainf   s>    

 �





r'   c                  C   sJ   t d�} | dks| dkr t�  n&| dks0| dkr8t�  ntd� | �  d S )Nz([1;0;40m
Do You want use again (y/n) - �y�Y�n�Nz[1;31;40mEnter valid letter)r   r'   �quitr   )r   r%   r%   r&   r   �   s    r   �__main__)r   Zurllibr   r   r   r   r   r   r   r   �open�f�readr   �closer   r   Zwrr   r   r   �ImportErrorZauthr'   r   �__name__r%   r%   r%   r&   �<module>   s^   
.














'
